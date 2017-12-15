var cart = [];

function getCart() {
 return cart;
}

function setCart(c) {
  cart = c;
  return cart;
}

function addToCart(item) {
  var itemPrice = Math.floor((Math.random()*100)+1);
  var itemName = item;
cart.push([itemName]: itemPrice)
console.log(`${item} has been added to your cart.`)
 return cart
}
