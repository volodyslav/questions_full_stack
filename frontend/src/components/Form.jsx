import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../api';
import { ACCESS_TOKEN, REFRESH_TOKEN } from '../constants';

const Form = ({route, method}) => {
    const [loading, setLoading] = useState(false);
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [password2, setPassword2] = useState("");

    const navigate = useNavigate();

    // When you register you login in the same time
    const loginAndRegister = async (routeFunc, username, password) => {
        const resLogin = await api.post(routeFunc, {username, password})
        localStorage.setItem(ACCESS_TOKEN, resLogin.data.access)
        localStorage.setItem(REFRESH_TOKEN, resLogin.data.refresh)
        navigate("/")
    }

    const name = method === "login" ? "Login" : "Register"

    const handleSubmit = async(e) => {
        setLoading(true);
        e.preventDefault();
        try{
            if (method === "login"){
                loginAndRegister(route, username, password)
            }else if(method === "register"){
                await api.post(route, {username, password, password2})
                loginAndRegister("/api/token", username, password)
            }else{
                navigate("/login")
            } 
        }catch(error){
            console.log(error)
        }finally{
            setLoading(false)
        }
    }


  return (
    <div className=' flex justify-center my-10 p-4 border rounded-2xl shadow-2xl w-fit mx-auto'>
        <form onSubmit={handleSubmit}>
            <h1 className=' text-2xl my-4 flex justify-center'>{name}</h1>
            <div>{loading && <p>Loading...</p>}</div> 
            <div className='my-4 text-center'>
                <input type="text" placeholder='Username' value={username} maxLength={50} minLength={5} onChange={(e) => setUsername(e.target.value)}></input>
                <input type="password" placeholder='Password' maxLength={30} minLength={5} value={password} onChange={(e) => setPassword(e.target.value)}></input>
                {method === "register" && <input type="password" placeholder='Repeat password' maxLength={30} minLength={5} value={password2} onChange={(e) => setPassword2(e.target.value)}></input>}
            </div>
            <button type='submit' className='text-white text-2xl my-4 flex p-2 justify-center bg-green-900 hover:bg-green-800 duration-300 ease-in-out hover:scale-105 rounded-xl'>Submit</button>
        </form>
    </div>
  )
}

export default Form