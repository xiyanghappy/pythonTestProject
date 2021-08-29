import Vue from 'vue'
import VueRouter from 'vue-router'
import Testcase from '../views/Testcase'
import Layout from "../views/Layout";
import Task from "../views/Task";

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location){
  return originalPush.call(this, location).catch(err => err)
}

Vue.use(VueRouter)


const routes = [
  {
    path: '/',
    redirect:'/layout'
  },
  {
    path: '/layout',
    name: 'layout',
    component: Layout,
    children:[
      {
        path: 'testcase',
        name: 'testcase',
        component: Testcase
      },
      {
        path: 'task',
        name: 'task',
        component: Task
      },
    ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
