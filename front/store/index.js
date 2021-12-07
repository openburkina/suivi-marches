import axios from 'axios'

export const state = () => ({
    list: null,
    recordsDone: null,
    recordsInprogress:null
  })

export const mutations = {
    listOfBuyers(state,paylaod){
        state.list = paylaod
    },

    listRecordsDone(state,paylaod){
        state.recordsDone = paylaod
        console.log(state.recordsDone)
    },
    listRecordsInprogress(state,paylaod){
        state.recordsInprogress = paylaod
        console.log(state.recordsInprogress)

    }
    
}
export const actions = {
    async fetchBuyers({ commit }){
        await axios.get(
            "http://localhost:8000/api/buyers",
          ).then(res=>{
              commit("listOfBuyers",res.data)}
        )
    },

    async recordsDone({commit},id){
        await axios.get(
            `http://localhost:8000/api/buyers/${id}/records/done/`)
            .then(res=>{
                commit("listRecordsDone",res.data)
            })
    },
    async recordsInprogress({commit},id){
        await axios.get(
            `http://localhost:8000/api/buyers/${id}/records/in_progress/`)
            .then(res=>{
                commit("listRecordsInprogress",res.data)
            })
    },
}
export const getters = {}

