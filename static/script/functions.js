var carts={};
if (localStorage.getItem("carts")) {
    carts = JSON.parse(localStorage.getItem("carts"));
}

function addToCart(productId,price,qty){
   
    let cartItem = {productId:productId, price:price, qty:qty};
    carts[productId]=cartItem;
    localStorage.setItem("carts", JSON.stringify(carts));
    alert("ajouter au panier réussi!");
}


function cleanCart(carts){

    localStorage.removeItem(carts);

}