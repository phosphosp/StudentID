const { test, expect } = require('@playwright/test');

test('should submit form and render display page', async ({ page }) => {
  // 1. Go to the Flask home page
  await page.goto('http://127.0.0.1/');

  // 2. Fill in the input field
  await page.fill('input[name="user_input"]', 'admin');

  // 3. Click the submit button
  await page.click('button[type="submit"]');

  // 4. Wait for the redirect and check the result page
  await expect(page).toHaveURL(/\/submit/);

  // 5. Check that the result is rendered
  await expect(page.locator('body')).toContainText('admin');
});