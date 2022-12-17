document.querySelector("#jsfetch").addEventListener("click", Handler);

function Handler(event) {
    fetch('/apiq')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            console.log(myjson);
        });
}
