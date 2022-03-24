// load projects
let PROJECTS = {}
const http = new XMLHttpRequest()
http.open("GET", "http://localhost:8008/get-projects")
http.send()
http.onreadystatechange = (e) => {
    if (http.readyState == XMLHttpRequest.DONE) {
        PROJECTS = JSON.parse(http.responseText)["projects"]
    }
}
// Add-project button
const add_project_button = document.querySelector(".nav__header__button")
const add_project_prompt = document.querySelector(".add-project-prompt")

add_project_button.addEventListener("click", (event) => {
    console.log("click button")
    add_project_prompt.classList.remove("invisible")
})

add_project_prompt.addEventListener("click", (event) => {
    if (event.target !== add_project_prompt) { return }
    console.log("click prompt background")
    add_project_prompt.classList.add("invisible")
})

// when you click the background part of the prompt the prompt closes
// the form sends new project data to server
// call reload projects function