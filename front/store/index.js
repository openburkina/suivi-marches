import axios from 'axios'

export const state = () => ({
    list: [],
    recordsDone: [],
    recordsInprogress:[],
    totauxByBuyer:[],
    records:[],
    tendersYear:[],
    bByRegion:[],
    listOfCleanData:[],
    
  })

export const mutations = {

    // setter de Liste de tous les buyers
    listOfBuyers(state,paylaod){
        state.list = paylaod
        state.list.forEach(el => {
            console.log(el)
            state.listOfCleanData.push({
                id:el.id,
                name:el.name,
                country_name:el.address.country_name,
                locality:el.address.locality,
                latitude:el.address.locality_latitude,
                longitude:el.address.locality_longitude,
                postal:el.address.postal_code,
                region:el.address.region,
                email:el.contact_point.email,
                fax_number:el.contact_point.fax_number,
                contact_name:el.contact_point.name,
                telephone:el.contact_point.telephone,
                url:el.contact_point.url,
                uri:el.identifier.uri,
                scheme:el.identifier.scheme,
                legal_name:el.identifier.legal_name,
            })
            
        })
        state.list = state.listOfCleanData
        state.listOfCleanData = []
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

    },
    
    // setter de Liste de tous les travauxd'un buyers par region
    listTotauxBuyer(state,paylaod){
        state.totauxByBuyer = paylaod
        console.log(state.totauxByBuyer)

    },
    // setter de Liste de tous les tenders
    listSpecification(state,paylaod){
        state.records = paylaod
        console.log(state.records)

    },
    // setter de Liste de tous les marché par année
    listTendersByYear(state,paylaod){
        state.tendersYear = paylaod
        console.log(state.tendersYear)

    },

     // setter de Liste de tous les marché par année
    listBuyerByRegion(state,paylaod){
        state.bByRegion = paylaod
        console.log(state.bByRegion)

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

    async allRecordsInprogress({commit}){
        await axios.get(
            `http://localhost:8000/api/buyers/records/in_progress/`)
            .then(res=>{
                commit("listRecordsInprogress",res.data)
        })
    },

    /*
        ###################################################################
    */
    // Liste de tous les totaux encore et terminé par buyers
    async tendersBuyer({commit},id){
        await axios.get(
            `http://localhost:8000/api/buyers/${id}/records/total`)
            .then(res=>{
                commit("listTotauxBuyer",res.data)
        })
    },
    /*
        ###################################################################
    */
    // Liste de tous les specification
    async specification({commit}){
        await axios.get(
            `http://localhost:8000/api/records`)
            .then(res=>{
                commit("listSpecification",res.data)
        })
    },
    /*
        ###################################################################
    */
    // Liste de tous les marchés et leurs etats
    async tendersByYear({commit},year){
        await axios.get(
            `http://localhost:8000/api/tenders/year/${year}/tender_state`)
            .then(res=>{
                commit("listTendersByYear",res.data)
        })
    },

    /*
        ###################################################################
    */
    // Liste de tous les buyers par regions
    async buyerByRegion({commit},year){
        await axios.get(
            `http://localhost:8000/api/buyers/${year}/total_by_region`)
            .then(res=>{
                commit("listBuyerByRegion",res.data)
        })
    },
    

}
export const getters = {}

