// const myModal = document.getElementById('myModal')
// const myInput = document.getElementById('myInput')
//
// myModal.addEventListener('shown.bs.modal', function () {
//     myInput.focus()
// })
// import dotenv from "dotenv";
import axios from 'axios'

$('#callme').click(() => {
    const name = document.getElementById('name').value
    const phone = document.getElementById('number').value
    console.log(name, phone)
    axios.post('http://localhost:8080/sendmsg', {name, phone})
    // const transporter = nodemailer.createTransport({
    //     host: "smtp.yandex.ru",
    //     port: 465,
    //     secure: true, // upgrade later with STARTTLS
    //     auth: {
    //         user: "evgeniy.tikhonenkov@yandex.ru",
    //         pass: "SysopZareval80!",
    //     },
    // });
    // transporter.verify(function (error, success) {
    //     if (error) {
    //         console.log(error);
    //     } else {
    //         console.log("Server is ready to take our messages");
    //     }
    // });

})