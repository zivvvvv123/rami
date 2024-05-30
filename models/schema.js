const mongoose = require("mongoose");

const productSchema = new mongoose.Schema(
  {
    product_name: { type: String },
    price_per_kg: { type: String },
    price: { type: String },
    unitPrice: { type: String },
    quantity: { type: String },
    brand: { type: String },
    supermarket: { type: String },
    discount: { type: String },
    productLink: { type: String },
    image_url: { type: String },
  },
  { collection: "juhananof" }
); // Specify the collection name here

const Product = mongoose.model("Product", productSchema);

module.exports = Product;
