import Oct8 from "./Oct8/Oct8/Oct8.js"

let oct8 = new Oct8()

function PaginaPrincipal(){
    if(window.location.hash)
    {
        
        NotFoundPage()
    }
    else
    {
        oct8.ModifyContentContainer(document.getElementById("Pagina_projeto"),`
        <h1> Analise de dados </h1>
        <article>
            <div><a href='http://127.0.0.1:5000/#/dados'>Analise por Graficos</a></div>
            <div>Analise dos dados</div>
            <div>Modelos de analise</div>
        <article>
        `,true)
    }

}

function dadosPagina(){
    fetch("http://127.0.0.1:5000/dados")
    .then(response =>response.json())
    .then(json =>{
        console.log(json)
        oct8.ModifyContentContainer(document.getElementById("Pagina_projeto"),`
        <h1>Listagem da massa de dados</h1>
        <div id='ListaDados'></div>
        `,true)
        let ListaDados = json.Dados_3040.Dados

        ListaDados.forEach(element=>{
            oct8.ModifyContentContainer(document.getElementById("ListaDados"),`
                <div class='data_value'>${element}</div>
            `)
        })

    })
    
}

function PaginaSobre(){
    oct8.ModifyContentContainer(document.getElementById("Pagina_projeto"),`
    <h1>Criador do propjeto</h1>
    <h3>Projeto criado e mantido por felipe Catão, analista de sistemas e desenvolvedor
    python a mais de 4 anos.</h3>
    `,true)
}

function PaginaLogin(){
    oct8.ModifyContentContainer(document.getElementById("Pagina_projeto"),`
    <form>
    <label>Nome </label><input id='input_user' type='text'></input>
    <button id='conId'>Conectar</button>
    <div class='aviso'></div>
    </form>
    `,true)
    
    document.getElementById('conId').addEventListener("click",()=>{
        fetch("http://127.0.0.1:5000/login",{method:"GET",
        headers: {'Authorization': 'Basic ' + btoa(document.getElementById('input_user').value+':'+'00')}})
        .then(response =>response.json(),Headers)
        .then(json =>{
            let valueUser = document.getElementById('input_user').value
            console.log(json)
            if(json['Status'] != 'Logado com sucesso')
            {
                document.getElementsByClassName('aviso')[0].innerHTML="Falha ao conectar!"
            }
            else
            {
                window.location.href = "http://127.0.0.1:5000/#/dados"
            }
        })})
}

function NotFoundPage(){
    oct8.ModifyContentContainer(document.getElementById("Pagina_projeto"),`
    <h1>404</h1>
    <h3>Essa pagina não existe 😑</h3>
    `,true)
}


oct8.CreateNewRoute("/sobre",PaginaSobre)
oct8.CreateNewRoute("/dados",dadosPagina)
oct8.CreateNewRoute("/login",PaginaLogin)
oct8.AddNotFoundPage(PaginaPrincipal)
oct8.LoadRoutes()
