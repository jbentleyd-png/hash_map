# frozen_string_literal: true
require_relative '../lib/hashmap'
describe  do
  describe "hash" do
    it "creates a code with the name Rama" do
      test = HashMap.new
      
      expect(test.hash('Rama')).to eq(test.hash('Sita'))
    end
  end
end
# this seems to have been a pure hypothetical