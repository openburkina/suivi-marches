import axios from 'axios'

export const state = ()=>({
    buyers: null,
    token : "",
  
})

export const mutations = {
    listOfBuyers({state,paylaod}){
        state.buyers = paylaod
    },

    setToken({state,paylaod}){
        state.token = paylaod
    }
    
}
export const actions = {
    async getToken({commit}){
        await axios.post("http://0.0.0.0:8000/auth-token/",
        {"username":"AdamMusa","password":"Adaforlan"}
        ).then((res)=>commit('setToken',res.data.token))
    },
    async fetchBuyers({commit}){
       await axios.get('https://randomuser.me/api/',
       {
        headers: {
            "Content-Type": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
            }
          }
       ).then((res)=>{commit('listOfBuyers',res.data)}).catch((err)=>console.log(err))
        
       
    }
}
export const getters = {}