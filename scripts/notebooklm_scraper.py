import asyncio
import os
from playwright.async_api import async_playwright

# Configuration
USER_DATA_DIR = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default") # Example path for Mac Chrome
NOTEBOOK_URL = "https://notebooklm.google.com/" # User needs to provide specific notebook URL
OUTPUT_DIR = "/Users/jiookcha/Library/CloudStorage/OneDrive-Personal/_Documents/_그랜트/00베리타스/01summaries/notebooklm_insights"

async def run():
    async with async_playwright() as p:
        # Note: Using launch_persistent_context to reuse login session
        # User MUST close their regular Chrome instance before running this or use a separate profile
        try:
            browser = await p.chromium.launch_persistent_context(
                user_data_dir=USER_DATA_DIR,
                headless=False, # Set to True for background runs once working
                args=["--disable-blink-features=AutomationControlled"]
            )
            
            page = await browser.new_page()
            await page.goto(NOTEBOOK_URL)
            
            print("Navigated to NotebookLM. Please ensure you are logged in.")
            
            # Wait for the notes list to appear (Selector depends on NotebookLM UI)
            # This is a template; specific selectors will need refinement based on current UI
            await page.wait_for_selector("text='Saved Notes'", timeout=30000)
            
            # Example: Iterate through notes and save them
            notes = await page.query_selector_all(".note-item-class") # Mock selector
            
            for i, note in enumerate(notes):
                title = await note.inner_text()
                await note.click()
                # Extract content from the active note panel
                content = await page.inner_text(".note-content-class") # Mock selector
                
                filename = f"note_{i}_{title[:20]}.md"
                with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
                    f.write(f"# {title}\n\n{content}")
                    
            await browser.close()
            print("Scraping completed.")
            
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    asyncio.run(run())
