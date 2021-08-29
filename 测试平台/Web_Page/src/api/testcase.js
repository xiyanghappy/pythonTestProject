import axios from "./http";
const testcase = {
    getTestcase() {
        return axios({
            method: 'get',
            url: '/testcase',
        })
    },
    delTestcase(params) {
        return axios({
            method: 'delete',
            url: '/testcase',
            params: {'id':params}
        })
    },
    createTestcase(params) {
        return axios({
            method: 'post',
            url: '/testcase',
            data: params
        })
    },
    editTestcase(params) {
        return axios({
            method: 'put',
            url: '/testcase',
            data: params
        })
    },
}
export default testcase