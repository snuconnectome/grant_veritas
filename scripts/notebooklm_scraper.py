import asyncio
import os
from playwright.async_api import async_playwright

# Configuration
USER_DATA_DIR = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default")
NOTEBOOK_URL = "https://notebooklm.google.com/notebook/644472d6-3a23-45a7-8d7c-7f218e7c14b4"
OUTPUT_DIR = "/Users/jiookcha/Library/CloudStorage/OneDrive-Personal/_Documents/_그랜트/00베리타스/01summaries/notebooklm_insights"

async def run():
    async with async_playwright() as p:
        try:
            # Using persistent context to handle session/login
            context = await p.chromium.launch_persistent_context(
                user_data_dir=USER_DATA_DIR,
                headless=False, # Headed mode is better for user monitoring during sync
                args=["--disable-blink-features=AutomationControlled"]
            )
            
            page = await context.new_page()
            print(f"Navigating to {NOTEBOOK_URL}...")
            await page.goto(NOTEBOOK_URL)
            
            # 1. Click the '스튜디오' (Studio) tab
            # The selector identified by the subagent: mat-tab-group-0-label-2
            print("Switching to Studio tab...")
            await page.wait_for_selector("#mat-tab-group-0-label-2", timeout=30000)
            await page.click("#mat-tab-group-0-label-2")
            
            # 2. Wait for the list of notes (artifacts)
            await page.wait_for_selector(".artifact-button-content", timeout=15000)
            notes_elements = await page.query_selector_all(".artifact-button-content")
            print(f"Found {len(notes_elements)} saved notes.")
            
            for i in range(len(notes_elements)):
                # Re-query elements periodically to avoid stale element references
                current_notes = await page.query_selector_all(".artifact-button-content")
                note = current_notes[i]
                
                # Get the title from parent or children if needed
                note_title_raw = await note.inner_text()
                note_title = "".join(x for x in note_title_raw if x.isalnum() or x in " -_").strip()
                
                print(f"[{i+1}/{len(notes_elements)}] Processing: {note_title}")
                
                await note.click()
                
                # 3. Wait for content panel to load
                await page.wait_for_selector(".artifact-content-scrollable", timeout=10000)
                
                # Extract Title from the formal input field and Content from the panel
                formal_title = await page.input_value(".artifact-title") if await page.query_selector(".artifact-title") else note_title
                content = await page.inner_text(".artifact-content-scrollable")
                
                # Save as Markdown
                safe_filename = f"{i+1:02d}_{note_title[:30]}.md"
                with open(os.path.join(OUTPUT_DIR, safe_filename), "w", encoding="utf-8") as f:
                    f.write(f"# {formal_title}\n\n{content}")
                
                # 4. Click '뒤로' (Back) button to return to the list
                await page.click("button[aria-label='뒤로']")
                await page.wait_for_selector(".artifact-button-content", timeout=10000)

            await context.close()
            print("\nSync completed successfully.")
            
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Tip: Make sure all existing Chrome instances are closed before running the script.")

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    asyncio.run(run())
