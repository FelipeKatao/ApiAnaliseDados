fetch("http://127.0.0.1:5000/dadosbrutos/cliente").then(response => response.json())
.then(json =>{
    let ListaClienteBruto = json
    let ClientesFiltrados = []
    ListaClienteBruto.forEach(element => {
            ClientesFiltrados.push({
                "Id":element[0],
                "Nome":element[1],
                "Data":element[2]
            })
        })
    console.log(ListaClienteBruto)
    console.log(ClientesFiltrados)
    ClientesFiltrados.forEach(clientes=>{
        document.getElementById("dados").innerHTML+=`<div class='card'>
        <h1>`+clientes["Nome"]+`</h1>
        <h2>`+clientes["Data"]+`</h2>
        </div>
        `
    })
    });



import sessionBase from "./session";

let se = sessionBase()
se.functionBase()