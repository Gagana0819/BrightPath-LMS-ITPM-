/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        base: '#F8FAFC',
        surface: '#FFFFFF',
        content: '#0F172A',
        brand: {
          DEFAULT: '#2563EB',
          hover: '#1D4ED8',
        },
        accent: {
          DEFAULT: '#F59E0B',
          hover: '#D97706',
        },
        hero: {
          bg: {
            left: '#F8FAFC',     // Left light background
            right: '#97C4C4',    // Right dark angled background
            shape1: '#d5e2fc',   // Floating blocks color 1
            shape2: '#faefff',   // Background pinkish wedge
            pill: '#e4f8f6',     // Navbar pill greenish cyan
          },
          highlight: '#5D6DFF',  // Main vibrant title text & shapes
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        'xl': '1rem',
        '2xl': '1.5rem',
      }
    },
  },
  plugins: [],
}
