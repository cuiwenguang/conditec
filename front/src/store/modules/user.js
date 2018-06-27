import axios from 'axios'
import request from '@/utils/request'
import { getToken, setToken, removeToken } from '@/utils/auth'

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
        axios({
          method: 'post',
          url: '/api/auth/',
          baseURL: process.env.BASE_API, // api的base_url
          timeout: 15000, // 请求超时时间
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
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
          commit('SET_TOKEN', res.data.token)
          setToken(res.data.token)
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
      return new Promise((resolve, reject) => {
        request.get('/api/system/users/0/')
          .then(function(res) {
            commit('SET_USERNAME', res.username)
            commit('SET_USERNAME', res.first_name)
            commit('SET_USERNAME', res.last_name)
            commit('SET_AVATAR', '')
            commit('SET_ROLES', res.groups)
            resolve(res)
          })
          .catch(error => reject(error))
      })
    },

    // 登出
    FedLogOut({ commit }) {
      return new Promise(resolve => {
        commit('SET_TOKEN', '')
        removeToken()
        resolve()
      })
    }
  }
}

export default user
