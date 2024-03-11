/** @type {import('tailwindcss').Config} */
const plugin = require('tailwindcss/plugin')
const colors = require('tailwindcss/colors')
module.exports = {
  content: ["./Template1/templates/myBlog/*.html", "./node_modules/flowbite/**/*.js"],
  theme: {
    colors: {
      primary: "#1E429F",
    },
    extend: {},
  },
  plugins: [require("flowbite/plugin"), plugin(function ({ addComponents, theme }) {
    addComponents({
      '.container': {
        maxWidth: theme('columns.7xl'),
        marginLeft: 'auto',
        marginRight: 'auto',
        paddingLeft: theme('spacing.3'),
        paddingRight: theme('spacing.3'),
        '@screen sm': {
          paddingLeft: theme('spacing.4'),
          paddingRight: theme('spacing.4')
        }
      }
    })
  }),],
};
