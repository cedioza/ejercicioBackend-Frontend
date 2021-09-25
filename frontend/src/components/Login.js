import React, { useState, useEffect, useRef } from "react";

const API = process.env.REACT_APP_API;
export const Login = () => {

    const [email, setEmail] = useState ("")
    const [password, setPassword] = useState ("")

    const handleSubmit = async (e) => {
        e.preventDefault();

        const res = await fetch(`${API}/login`,{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email,
                password
            })
        })
        const data = await res.json();
        console.log(data)
        setEmail("");
        setPassword("");
        alert(data)
    }

    return (
        <div className="d-flex justify-content-center">
            <form onSubmit={handleSubmit} className="d-flex justify-content-center flex-column my-4 p-4">
                <h2 className="text-center">Formulario Login</h2>
                <input 
                onChange={e =>setEmail(e.target.value)}
                value={email}
                className="rounded-pill p-2 my-2"
                type="email"
                placeholder="Email"/>

                <input
                onChange={e =>setPassword(e.target.value)}
                value={password}
                className="rounded-pill p-2 my-2"
                type="password"
                placeholder="Password"/>

                <button className="btn btn-success">Enviar</button>
            </form>
        </div>
    )
}