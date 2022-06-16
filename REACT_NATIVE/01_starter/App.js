import { createAppContainer }   from "react-navigation"
import { createStackNavigator } from "react-navigation-stack"
import HomeScreen               from "./src/screens/HomeScreen"
import ComponentsScreen         from "./src/screens/ComponentsScreen"
import ListScreen               from "./src/screens/ListScreen"
import ImageScreen              from "./src/screens/ImageScreen"
import StateOneScreen           from "./src/screens/StateOneScreen"

const navigator = createStackNavigator(
  {
    Home      : HomeScreen,
    Components: ComponentsScreen,
    List      : ListScreen,
    Image     : ImageScreen,
    StateOne  : StateOneScreen,
  },
  {
    initialRouteName: "Home",
    defaultNavigationOptions: {
      title: "App",
    },
  }
);

export default createAppContainer(navigator);
