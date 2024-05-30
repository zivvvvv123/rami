const fs = require("fs");
const path = require("path");
const connectDB = require("../config/db");
const Product = require("../models/schema");

const importData = async () => {
  await connectDB();

  try {
    await Product.deleteMany();

    const productsJsonPath = path.join(
      __dirname,
      "..",
      "productsData",
      "products.json"
    );
    const jsonData = JSON.parse(fs.readFileSync(productsJsonPath, "utf8"));

    await Product.insertMany(jsonData);

    console.log("Data imported successfully");
    process.exit();
  } catch (err) {
    console.error("Error importing data:", err);
    process.exit(1);
  }
};

importData();
