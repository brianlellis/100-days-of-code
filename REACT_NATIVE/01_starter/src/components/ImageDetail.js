import React from 'react'
import { Text, StyleSheet, View, Image } from 'react-native'

const ImageDetail = props => (
  <View>
    {/* https://reactnative.dev/docs/images */}
    <Image 
      source={{ uri: props.url }} 
      style={{ width: 100, height: 100 }}
    />
    <Text>{props.title}</Text>
  </View>
)

const styles = StyleSheet.create({
  textStyle: {
    fontSize: 30
  }
})

export default ImageDetail