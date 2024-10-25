const { Builder, By, until } = require('selenium-webdriver');
const { assert } = require('chai');

describe('Google Search Page', function() {
    let driver;

    // Setup the browser before each test
    before(async function() {
        driver = await new Builder().forBrowser('chrome').build();
    });

    // Close the browser after each test
    after(async function() {
        await driver.quit();
    });

    it('should load the Google homepage', async function() {
        await driver.get('https://www.google.com'); // Navigate to Google
        const title = await driver.getTitle(); // Get the page title
        assert.equal(title, 'Google'); // Assert that the title is correct
    });

    it('should perform a search and display results', async function() {
        await driver.get('https://www.google.com'); // Navigate to Google
        const searchBox = await driver.findElement(By.name('q')); // Locate the search box
        await searchBox.sendKeys('Selenium WebDriver'); // Type in the search query
        await searchBox.submit(); // Submit the search form

        // Wait for the results page to load and display results
        await driver.wait(until.titleContains('Selenium WebDriver'), 5000);
        const title = await driver.getTitle(); // Get the page title after search
        assert.include(title, 'Selenium WebDriver'); // Assert that the title contains the search query
    });
});

