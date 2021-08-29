import axios from "./http";
const task = {
    getTask() {
        return axios({
            method: 'get',
            url: '/task',
        })
    },

    addTask(params) {
        return axios({
            method: 'post',
            url: '/task',
            data: params
        })
    },
}
export default task