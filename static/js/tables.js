/*
const indicator = ['123', '345', '658'];
const table = document.querySelector('#table');

async function renderDataTable () {
table.innerHTML = '';
indicator.forEach(item => {
let sTr = document.createElement("tr");
sTr.innerHTML = `<td>${item}</td>`;

table.appendChild(sTr);
});
}

renderDataTable();
fillTable(table, indicator);
console.log(indicator);
*/

document.querySelector("#table");
function Handler(event) {
    fetch('/api')
        .then((response) => {
            console.log(response.json());
            return response.json();
        })
        .then((myjson) => {
            console.log(myjson);
        });
}