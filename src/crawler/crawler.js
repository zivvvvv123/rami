const puppeteer = require("puppeteer");
const fs = require("fs");
const path = require("path");

// Function to save HTML content to a file
async function savePageHTML(url, htmlContent, names) {
  const fileName = names[url] || "index"; // Use URL name or "index" if not found
  const directoryPath = path.join(__dirname, "..", "pages"); // Adjusted directory path
  const filePath = path.join(directoryPath, fileName + ".html");

  try {
    // Check if the directory exists, create it if it doesn't
    if (!fs.existsSync(directoryPath)) {
      fs.mkdirSync(directoryPath, { recursive: true });
    }

    await fs.promises.writeFile(filePath, htmlContent);
    console.log(`saved ${fileName}.html`);
  } catch (error) {
    console.error(`Error saving ${fileName}.html:`, error);
  }
}

// Empty array for URLs to visit
const urlsToVisit = [
  {
    url: "https://yochananof.co.il/s59/pirvt-virqvt.html",
    name: "fruits and vegetables",
  },
  {
    url: "https://yochananof.co.il/s59/mvcri-hlb-vbicim.html",
    name: "milk eggs and salads",
  },
  {
    url: "https://yochananof.co.il/s59/bwr-vdgim-triim.html",
    name: "meat",
  },
  {
    url: "https://yochananof.co.il/s59/mkvlt.html",
    name: "meholet",
  },
  {
    url: "https://yochananof.co.il/s59/qpvaim.html",
    name: "freezables",
  },
  {
    url: "https://yochananof.co.il/s59/mwqavt-iin-valkvhvl.html",
    name: "drinks ",
  },
  {
    url: "https://yochananof.co.il/s59/parm-vmvcri-tinvqvt.html",
    name: "pharm",
  },
  {
    url: "https://yochananof.co.il/s59/hvmri-niqvi-vhd-pemi.html",
    name: "cleaning",
  },
  {
    url: "https://yochananof.co.il/s59/sltim-vnqniqim.html",
    name: "salad and salami",
  },
  {
    url: "https://yochananof.co.il/s59/lhmim-vmapim.html",
    name: "baking",
  },
  {
    url: "https://yochananof.co.il/s59/nf.html",
    name: "one time use",
  },
];

(async () => {
  // Launch Puppeteer
  const browser = await puppeteer.launch();

  // Create a new page
  const page = await browser.newPage();

  // Initialize a set to keep track of visited URLs
  const visitedUrls = new Set();

  // Crawl each URL
  for (const { url, name } of urlsToVisit) {
    if (!visitedUrls.has(url)) {
      // Visit the URL
      await page.goto(url, { waitUntil: "networkidle2" }); // Wait for network activity to be idle

      // Wait for the specific selector to appear
      await delay(10000);

      // Continuously scroll until all products are loaded
      await autoScroll(page);

      // Get the page HTML content after it's fully loaded
      const htmlContent = await page.evaluate(
        () => document.documentElement.outerHTML
      );

      // Save the HTML content to a file with the specified name
      await savePageHTML(url, htmlContent, { [url]: name });

      // Add the URL to the set of visited URLs
      visitedUrls.add(url);
    }
  }

  // Close the browser
  await browser.close();

  // Function to continuously scroll until all products are loaded
  async function autoScroll(page) {
    let previousHeight = 0;
    let scrollAttempts = 0;
    const maxScrollAttempts = 60; // Adjust this value as needed

    while (scrollAttempts < maxScrollAttempts) {
      // Scroll to the bottom of the page
      await page.evaluate("window.scrollTo(0, document.body.scrollHeight)");

      // Wait for a short interval to allow content loading
      await delay(3000); // Wait for 4 seconds; adjust as needed

      // Get the current scroll height
      const currentHeight = await page.evaluate("document.body.scrollHeight");

      // If the current scroll height hasn't changed, it means all content is loaded
      if (currentHeight === previousHeight) {
        break;
      }

      // Update the previous scroll height and increment scroll attempts
      previousHeight = currentHeight;
      console.log(scrollAttempts, currentHeight);
      scrollAttempts++;
    }
  }

  // Function to create a delay
  function delay(time) {
    return new Promise((resolve) => {
      setTimeout(resolve, time);
    });
  }
})();
