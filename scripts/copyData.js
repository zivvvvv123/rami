const fs = require("fs");
const path = require("path");

const outputDir = path.join(__dirname, "..", "src", "output");
const productsDataDir = path.join(__dirname, "..", "productsData");

if (!fs.existsSync(productsDataDir)) {
  fs.mkdirSync(productsDataDir);
}

const files = fs.readdirSync(outputDir);

let allProducts = [];

for (const file of files) {
  const filePath = path.join(outputDir, file);

  const jsonData = JSON.parse(fs.readFileSync(filePath, "utf8"));

  allProducts = allProducts.concat(jsonData);
}

const productsJsonPath = path.join(productsDataDir, "products.json");
fs.writeFileSync(productsJsonPath, JSON.stringify(allProducts, null, 2));

console.log("Combined data written to products.json successfully.");
