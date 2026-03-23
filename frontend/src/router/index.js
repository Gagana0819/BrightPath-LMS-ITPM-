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
<<<<<<< HEAD
      component: () => import('../views/LoginView.vue'),
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue'),
=======
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
>>>>>>> 61542dc3466c944a72cf4825924e0c241bfa5b9c
    },
    {
      path: '/dashboard',
      component: () => import('../components/layout/MainLayout.vue'),
<<<<<<< HEAD
      children: [
        {
          path: '',
          name: 'dashboard_home',
=======
      meta: { requiresAuth: true },
      children: [
        {
          path: '',
          name: 'dashboard',
>>>>>>> 61542dc3466c944a72cf4825924e0c241bfa5b9c
          component: () => import('../views/DashboardView.vue'),
        },
        {
          path: 'library',
<<<<<<< HEAD
          name: 'dashboard_library',
=======
          name: 'library',
>>>>>>> 61542dc3466c944a72cf4825924e0c241bfa5b9c
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
          component: () => import('../views/ContentDashboard.vue'),
<<<<<<< HEAD
        }
      ]
    },
    {
      path: '/library',
      name: 'library',
      component: () => import('../views/LibraryView.vue'),
    },
  ],
})

=======
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
  } else if ((to.name === 'login' || to.name === 'register') && isAuthenticated) {
    // Redirect to dashboard if already authenticated
    next({ name: 'dashboard' });
  } else {
    next();
  }
});

>>>>>>> 61542dc3466c944a72cf4825924e0c241bfa5b9c
export default router
