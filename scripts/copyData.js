const fs = require("fs");
const path = require("path");

const outputDir = path.join(__dirname, "..", "src", "output");
const productsDataDir = path.join(__dirname, "..", "productsData");

// Create productsData directory if it doesn't exist
if (!fs.existsSync(productsDataDir)) {
  fs.mkdirSync(productsDataDir);
}

// Read all JSON files from the output directory
const files = fs.readdirSync(outputDir);

let allProducts = [];

// Loop through each file
for (const file of files) {
  const filePath = path.join(outputDir, file);

  // Read JSON data from the file
  const jsonData = JSON.parse(fs.readFileSync(filePath, "utf8"));

  // Merge data into the allProducts array
  allProducts = allProducts.concat(jsonData);
}

// Write the combined data to products.json
const productsJsonPath = path.join(productsDataDir, "products.json");
fs.writeFileSync(productsJsonPath, JSON.stringify(allProducts, null, 2));

console.log("Combined data written to products.json successfully.");
