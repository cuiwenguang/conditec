import axios from 'axios'
import { getToken, setToken } from '@/utils/auth'

const user = {
  state: {
    token: getToken(),
    username: '',
    name: '',
    job: '',
    avatar: '',
    roles: []
  },

  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
    },
    SET_USERNAME: (state, username) => {
      state.username = username
    },
    SET_NAME: (state, name) => {
      state.name = name
    },
    SET_JOB: (state, job) => {
      state.job = job
    },
    SET_AVATAR: (state, avatar) => {
      state.avatar = avatar
    },
    SET_ROLES: (state, roles) => {
      state.roles = roles
    }
  },

  actions: {
    // 登录
    Login({ commit }, userInfo) {
      return new Promise((resolve, reject) => {
        debugger
        axios({
          method: 'post',
          url: '/o/token/',
          baseURL: process.env.BASE_API, // api的base_url
          timeout: 15000, // 请求超时时间
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          auth: {
            username: 'xaU6yr60kA2HCQpnTwfC3X5ElXrb4ddRqo7zBADZ',
            password: '066kzs7bB3lTDQWIgXdSTYKBc9DXMne5pM6M4lLfVqmRqg35uvsk5GAuqRmXqBTkbG0ggqe4kFfdSQucxzYQfWFyZwnNfM2QsW0gM2VDbPzeecjbRQrLKZ0WCAK0VcXT'
          },
          data: userInfo,
          transformRequest: [function(items) {
            let ret = ''
            for (const it in items) {
              ret += encodeURIComponent(it) + '=' + encodeURIComponent(items[it]) + '&'
            }
            return ret
          }]
        }).then((res) => {
          debugger
          commit('SET_TOKEN', res.data.access_tokken)
          setToken(res.data.access_tokken)
          resolve()
        }).catch(err => {
          const ret = {
            status: 500,
            message: '服务器发生错误'
          }
          if (err.response.status === 400 || err.response.status === 401) {
            ret.status = err.response.status
            ret.message = '错误的用户名或密码'
          }
          reject(ret)
        })
      })
    },

    // 获取个人信息
    GetInfo({ commit }) {
      return {}
    } 
  }
}

export default user
