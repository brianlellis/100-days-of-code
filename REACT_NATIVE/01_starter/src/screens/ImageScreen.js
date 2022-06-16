import ImageDetail from '../components/ImageDetail'
import React       from 'react'
import { 
  Button,
  FlatList,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native'

const images = [
  { title: "Forest", url: "https://images.unsplash.com/photo-1448375240586-882707db888b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" },
  { title: "Desert", url: "https://images.unsplash.com/photo-1509316785289-025f5b846b35?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1476&q=80" },
  { title: "Glacier", url: "https://images.unsplash.com/photo-1516569422572-d9e0514b9598?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" },
  { title: "Mountain", url: "https://images.unsplash.com/photo-1544198365-f5d60b6d8190?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" },
  { title: "Beach", url: "https://images.unsplash.com/photo-1519046904884-53103b34b206?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80" },
]
// nested destructuring to extract props.navigation.navigate
const ImageScreen = ({ navigation: { navigate } }) => (
  <FlatList
    data={images}
    // If key not provided then full list will have to be deleted and re-rendered
    keyExtractor={ image => image.title }
    renderItem={ ({ item }) => (
      <ImageDetail title={item.title} url={item.url} />
    )}
  />
)

const styles = StyleSheet.create({
  text: {
    fontSize: 30,
  },
})

export default ImageScreen
