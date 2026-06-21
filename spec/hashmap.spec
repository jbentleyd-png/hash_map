# frozen_string_literal: true
require_relative '../lib/hashmap'
describe  do


  describe "hash" do
    it "simplifies to a bucket" do
      test = HashMap.new
      hash_code = test.hash('Benjamin')
      index = hash_code.abs % test.capacity
      p index
      expect(index).to be_between(0, 15).inclusive
    end
    
    it "Rama becomes '3'" do
      test = HashMap.new
      index = test.hash('Rama')
      expect(index).to eq(3)
    end


    it "Rama and Sita result in a collision" do
      test = HashMap.new
      index = test.hash('Rama')
      index_two = test.hash('Sita')
      expect(index).to eq(index_two)
    end

  end

  describe "set" do
    it "creates a node" do
      test = HashMap.new
      test.set('Rama', 4)
      
      expect(test.buckets[3].value).to eq(4)
    end




  end

end
# this seems to have been a pure hypothetical