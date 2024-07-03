import axios from 'axios'
import router from '@/router' // Importer votre instance de routeur VueJS

axios.defaults.baseURL = "http://localhost:5000"
axios.interceptors.response.use(
  (response) =>{ console.log(response); return response;},
  (error) => {
    console.log(error)
    if (error.response.status === 403 || error.response.status === 401) {
      router.push({name: "login-admin"})
    }
    return Promise.reject(error)
  }
)

axios.interceptors.request.use(
  (config) => {
    if (localStorage.getItem("token")) {
      config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

export default axios