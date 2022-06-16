import React from 'react'
import { 
  Button, 
  StyleSheet, 
  Text, 
  TouchableOpacity, 
  View, 
} from 'react-native'

// nested destructuring to extract props.navigation.navigate
const HomeScreen = ({ navigation: { navigate } }) => (
  <View>
    <Button 
      onPress={() => navigate('Components')}
      title="Go to Coms Demo" 
    />
    <Button 
      onPress={() => navigate('Image')}
      title="Go to Image Screen Demo" 
    />
    <TouchableOpacity
      onPress={() => navigate('List')}
    >
      <Text>Go to List Demo</Text>
    </TouchableOpacity>
  </View>
)

const styles = StyleSheet.create({
  text: {
    fontSize: 30,
  },
})

export default HomeScreen
