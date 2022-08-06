document.getElementById("button").addEventListener('click', Message); 
let list = document.getElementById('list');
let doneList = document.getElementById('doneList');

function Message() {
    let message = prompt("enter todo item");
    let li = document.createElement('li');
    li.innerText = message;
    let button = document.createElement('button');
    button.innerText = "Complete";
    li.appendChild(button);
    button.addEventListener('click', moveListItem);
    list.appendChild(li);
}

function moveListItem(element) { 
    let parent = element.target.parentElement; 
    if (list.contains(parent)) {
        element.target.innerText = "Delete";
        doneList.appendChild(parent);
    }
    else
        doneList.removeChild(parent);
}