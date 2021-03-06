import fetch from "node-fetch";

const text = 'hello'
const URL = 'http://localhost:8080/translate'
const data = {'trgt': 'es','text':text}
const params = {
    headers:{
        "Content-Type":"application/json charset=UTF-8"
    },
    body: JSON.stringify(data),
    method:"POST",
    mode: "no-cors"
}
fetch(URL, params)
    .then(function (response) {
        return response.json();
}).then(function (translated) {
    console.log('GET response:');
    console.log(translated.text);
})
