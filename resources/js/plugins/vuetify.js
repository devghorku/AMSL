import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)

const opts = {}

export default new Vuetify(
    {
    theme: {
        dark: false,
        themes: {
            light: {
                primary:'#1AABA5',
                lightWhite: '#F5F6FA',
                grayTxt: '#BABABB'
            }
        }
    }
}
)