import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue'),
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue'),
    },
    {
      path: '/forgot-password',
      name: 'forgot-password',
      component: () => import('../views/ForgotPassword.vue'),
    },
    {
      path: '/dashboard',
      component: () => import('../components/layout/MainLayout.vue'),
      meta: { requiresAuth: true },
      children: [
        {
          path: '',
          name: 'dashboard',
          component: () => import('../views/DashboardView.vue'),
        },
        {
          path: 'home',
          name: 'student-home',
          component: () => import('../views/StudentHomeView.vue'),
        },
        {
          path: 'library',
          name: 'library',
          component: () => import('../views/LibraryView.vue'),
        },
        {
          path: 'profile',
          name: 'profile',
          component: () => import('../views/ProfileView.vue'),
        },
        {
          path: 'kuppi',
          name: 'kuppi',
          component: () => import('../views/KuppiDashboardView.vue'),
        },
        {
          path: 'upload',
          name: 'upload-course',
          component: () => import('../views/ContentDashboard.vue'), // Placeholder
        },
        {
          path: 'grades',
          name: 'my-grades',
          component: () => import('../views/ContentDashboard.vue'), // Placeholder
        }
      ]
    },
  ],
})

// Navigation Guard
router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('access_token');
  
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      // Redirect to login if not authenticated
      next({ name: 'login' });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router
