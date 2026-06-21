# frozen_string_literal: true
require_relative '../lib/hashmap'
describe  do
  describe "hash" do
    it "creates a code with the name Rama" do
      test = HashMap.new
      
      expect(test.hash('Rama')).to eq(2539555)
    end

    it "simplifies to a bucket" do
      test = HashMap.new
      hash_code = test.hash('Rama')
      index = hash_code.abs % test.capacity
      p index
      expect(index).to be_between(0, 15).inclusive
    end


  end

  describe "generate indeces" do
    it "Rama becomes '3'" do
      test = HashMap.new
      index = test.generate_index(test.hash('Rama'))
      expect(index).to eq(3)
    end


    it "Rama and Sita result in a collision" do
      test = HashMap.new
      index = test.generate_index(test.hash('Rama'))
      index_two = test.generate_index(test.hash('Sita'))
      expect(index).to eq(index_two)
    end

  end

end
# this seems to have been a pure hypothetical