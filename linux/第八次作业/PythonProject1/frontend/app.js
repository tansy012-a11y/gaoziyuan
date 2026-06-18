fetch("http://localhost:8000/products")
.then(res => res.json())
.then(data => {

    let html = "";

    data.forEach(item => {

        html += `
        <div>
            ${item.name}
            ￥${item.price}
            <button onclick="buy(${item.id})">
                购买
            </button>
        </div>
        `;
    });

    document.getElementById(
        "products"
    ).innerHTML = html;
});

function buy(id){

    fetch(
        `http://localhost:8000/order/${id}`,
        {
            method:"POST"
        }
    )
}