let cartCount = 0;

const cartDisplay = document.getElementById("cart-count");
const addCartButtons = document.querySelectorAll(".add-cart");

addCartButtons.forEach(button => {

    button.addEventListener("click", () => {

        cartCount++;
        cartDisplay.innerText = cartCount;

        alert("Product added to cart successfully!");
    });
});
function login(){

    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if(username === "admin" && password === "1234"){

        localStorage.setItem("loggedIn", "true");

        window.location.href = "index.html";

    } else {

        document.getElementById("message").innerHTML =
        "Invalid Username or Password";
    }
}

function logout(){

    localStorage.removeItem("loggedIn");

    window.location.href = "login.html";
}