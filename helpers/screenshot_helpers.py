import os
from datetime import datetime
from pathlib import Path

SCREENSHOTS_DIR = "test_screenshots"

def save_screenshot_on_teardown(driver, test_id, report_status):

    Path(SCREENSHOTS_DIR).mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    sanitized_name = test_id.replace("::", "__").replace("/", "_")
    filename = f"{sanitized_name}_{report_status}_{timestamp}.png"

    save_path = Path(SCREENSHOTS_DIR) / filename

    try:
        driver.save_screenshot(str(save_path))

    except Exception as e:
        print(f"\nERROR: Ekran görüntüsü kaydedilmedi: {e}")