tailwind.config = {
  theme: {
    fontFamily: {
      "Rubik-Mono-One": ['Rubik Mono One', 'monospace']
    },
    extend: {
      colors:{
        'lime_green': '#49634B'
      },
      keyfremes:{
        OpenMenu:     {
          'from': { 'top': '-100vh'}, 
          'to': {'top': '0'}
        },
        CloseMenu:     {
          'from': { 'top': '0'}, 
          'to': {'top': '-100vh'}
        },
        OpenBasket:     {
          'from': { 'right': '-33vw'}, 
          'to': {'right': '0'}
        },
        CloseBasket:     {
          'from': { 'right': '0'}, 
          'to': {'right': '-33vw'}
        },
        animation:{
          'openMenu': 'OpenMenu 0.7s linear forwards',
          'closeMenu': 'CloseMenu 0.7s linear forwards',
          'openBasket': 'OpenBasket 0.7s linear forwards',
          'closeBasket': 'CloseBasket 0.7s linear forwards',

        }

      }
    },
  },
}

function getWidhtV() {
  let result = {}
  for (let i = 0; i < 101; i++){
    if ( i % 2 == 0 ){
      result[`${i}v`] = `${i}vw`
    }
  }
}

function getHeightV() {
  let result = {}
  for (let i = 0; i < 101; i++){
    if ( i % 2 == 0 ){
      result[`${i}v`] = `${i}vh`
    }
  }
}


tailwind.config.theme.extend.width = getWidhtV()
tailwind.config.theme.extend.height = getHeightV()