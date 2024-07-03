/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'tropical-rain-forest': { '700': '#0c7556' },
        'mercury': {
          '100': '#e6e6e6',
          '200': '#E6E5E5'
         },
    
      }
    },
  },
  plugins: [],
}

