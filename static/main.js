


function menu(){
    let modal = document.getElementById('menu')
    if (!modal.classList.contains('openMenu')){
        modal.classList.add('openMenu')
        modal.classList.remove('hidden')
        modal.classList.remove('closeMenu')
        setTimeout(() => {
            modal.classList.add('block')
        }, 700)
    }
    else {
        modal.classList.remove('openMenu')
        modal.classList.add('closeMenu')
        modal.classList.remove('block')
        setTimeout(() => {
            modal.classList.add('hidden')
        }, 700)
    }
}

function basket(){
    let modal = document.getElementById('basket')
    if (!modal.classList.contains('openBasket')){
        modal.classList.add('openBasket')
        modal.classList.remove('hidden')
        modal.classList.remove('closeBasket')
        setTimeout(() => {
            modal.classList.add('block')
        }, 700)
    }
    else {
        modal.classList.remove('openBasket')
        modal.classList.add('closeBasket')
        modal.classList.remove('block')
        setTimeout(() => {
            modal.classList.add('hidden')
        }, 700)
    }
}



function createTask(){
    let dataInput = document.getElementsByClassName('search')
    let task = document.getElementById('task')
    task.innerHTML = dataInput[0].value
}



fetch('https://fakestoreapi.com/products')
            .then(res=>res.json())
            .then(json=>{
                let products = document.getElementById('products')
                console.log(json)
                for(let product of json){
                    products.innerHTML += `
                    <div>
                        <div>
                            <img src="${product.image}">
                        </div>
                        <div>
                            <span>
                            ${product.title}
                            </span>
                        </div>
                        <div>
                            <span>
                            ${product.description}
                            </span>
                        </div>
                        <div>
                            <span>
                            ${product.rating.rate}
                            </span>
                        </div>
                        <div>
                            <span>
                            ${product.rating.count}
                            </span>
                        </div>
                        <div>
                            <span>
                            ${product.category}
                            </span>
                        </div>
                        <div>
                            <span>
                            ${product.price}
                            </span>
                        </div>
                    </div>
                    `
                }
    })



window.addEventListener("DOMContentLoaded", (event) =>{
    const addUser = document.getElementById('addUser');
    if (addUser) {
        addUser.addEventListener("click", ()=>{
            e.preventDefault();
            let form = new FormData(addUser)
                fetch('https://fakestoreapi.com/users',{
                method:"POST",
                body:JSON.stringify(
                    {
                        email: form.get('email'),
                        username:form.get('username'),
                        password:form.get('password'),
                        name:{
                            firstname:form.get('firstname'),
                            lastname:form.get('lastname'),
                        },
                        address:{
                            city:form.get('city'),
                            street:form.get('street'),
                            number:form.get('number'),
                        },
                        phone:form.get('phone')
                    }
                )
            })
                .then(res=>res.json())
                .then(json=>console.log(json))
                }
            )
            }
});

// let user = document.getElementById('addUser')

// user.addEventListener('submit',)


function add_user(a){
    let user = document.getElementById('addUser')
    console.log(new FormData(user))
    e.preventDefault();
    fetch('https://fakestoreapi.com/users',{
        method:"POST",
        body:JSON.stringify(
            {
                email:'John@gmail.com',
                username:'johnd',
                password:'m38rmF$',
                name:{
                    firstname:'John',
                    lastname:'Dae',
                },
                address:{
                    city:'kilcoole',
                    street:'7835 new road',
                    number:3,
                    zipcode:'12926-3874',
                    geolocation:{
                        lat:'',
                        long:'',
                    },
                },
                phone:'1-570-236-7033'
            }
        )
    })
        .then(res=>res.json())
        .then(json=>console.log(json))

}   