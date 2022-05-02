import Cookies from "./js.cookie.mjs"

// load projects
let PROJECTS = {}
const http = new XMLHttpRequest()
http.open("GET", `${window.location.href}/get-projects`)
http.send()
http.onreadystatechange = (e) => {
    if (http.readyState == XMLHttpRequest.DONE) {
        PROJECTS = JSON.parse(http.responseText)["projects"]
        create_projects_list()
        if (Cookies.get("active_project")) {
            set_active_project(Cookies.get("active_project"))
        }
    }
}

// Open-menu button
const nav = document.querySelector("nav")
const open_menu_button = document.querySelector(".open-menu")

open_menu_button.addEventListener("click", (event) => {
    nav.classList.toggle("invisible")
})

//// display page
let active_project = null
const projects_list = document.querySelector(".nav__list")
const project_title = document.querySelector(".main__header__title")
const project_body = document.querySelector(".main__list")
const form_active_project = document.querySelector("#form-active-project")

function set_active_project(title) {
    active_project = title
    form_active_project.value = title
    Cookies.set("active_project", title)
    show_active_project()
}

function show_active_project() {
    // Set title
    project_title.innerText = active_project
    // Remove previous points
    while (project_body.lastElementChild) {
        project_body.removeChild(project_body.lastElementChild)
    }
    PROJECTS[active_project].forEach((point_text, i) => {
        const point = document.createElement("div")
        point.classList.add("main__list__item")
        point.innerText = point_text
        project_body.appendChild(point)
    })
}

function create_projects_list() {
    Object.keys(PROJECTS).forEach((title, i) => {
        const project = document.createElement("div")
        project.classList.add("nav__list__item")
        project.innerText = title

        project.addEventListener("click", (event) => {
            set_active_project(title)
            nav.classList.toggle("invisible")
        })

        projects_list.appendChild(project)
    })
}

// add-project button
const add_project_button = document.querySelector(".nav__header__button")
const add_project_prompt = document.querySelector(".add-project-prompt")

add_project_button.addEventListener("click", (event) => {
    add_project_prompt.classList.remove("invisible")
})

add_project_prompt.addEventListener("click", (event) => {
    if (event.target !== add_project_prompt) { return }
    add_project_prompt.classList.add("invisible")
})

// set cookie on new project submit
const add_project_form = document.querySelector("#add-project")
const add_project_name = document.querySelector("#name")

add_project_form.addEventListener("submit", (event) => {
    Cookies.set("active_project", add_project_name.value)
})