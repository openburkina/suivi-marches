import axios from 'axios'

export const state = () => ({
    list: null,
    recordsDone: [],
    recordsInprogress:[]
  })

export const mutations = {

    // setter de Liste de tous les buyers
    listOfBuyers(state,paylaod){
        state.list = paylaod
    },
    
    // setter de Liste de tous les travaux fait par un buyers
    listRecordsDone(state,paylaod){
        state.recordsDone = paylaod
        console.log(state.recordsDone)
    },

    // setter de Liste de tous les travaux en cours par buyers
    listRecordsInprogress(state,paylaod){
        state.recordsInprogress = paylaod
        console.log(state.recordsInprogress)

    }
    
}
export const actions = {
    /*
        ###################################################################
    */
    // Liste de tous les buyers
    async fetchBuyers({ commit }){
        await axios.get(
            "http://localhost:8000/api/buyers",
          ).then(res=>{
              commit("listOfBuyers",res.data)}
        )
    },
     /*
        ###################################################################
    */
    // Liste de tous les travaux fait par un buyers
    async recordsDone({commit},id){
        await axios.get(
            `http://localhost:8000/api/buyers/${id}/records/done/`)
            .then(res=>{
                commit("listRecordsDone",res.data)
            })
    },
    /*
        ###################################################################
    */
    // Liste de tous les travaux en cours par buyers
    async recordsInprogress({commit},id){
        await axios.get(
            `http://localhost:8000/api/buyers/${id}/records/in_progress/`)
            .then(res=>{
                commit("listRecordsInprogress",res.data)
            })
    },
}
export const getters = {}

