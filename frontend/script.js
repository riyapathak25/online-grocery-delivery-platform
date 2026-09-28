async function loadProducts() {
    const container = document.getElementById("products");

    container.innerHTML = "<p>Loading...</p>";

    try {
        const response = await fetch("/api/product/");

        if (!response.ok) {
            throw new Error("Unable to connect to Product Service");
        }

        const data = await response.json();

        container.innerHTML = `
            <div class="product">
                <h3>${data.service}</h3>
                <p>Status: ${data.status}</p>
                <p>${data.message}</p>
            </div>
        `;

    } catch (error) {
        container.innerHTML = `
            <div class="product">
                <h3>Connection Error</h3>
                <p>${error.message}</p>
            </div>
        `;
    }
}