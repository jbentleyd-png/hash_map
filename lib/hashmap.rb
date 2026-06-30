require_relative 'node'

class HashMap
  attr_accessor :capacity, :buckets
  
  def initialize(capacity = 16)
    @load_factor = 0.75
    @capacity = capacity
    @buckets = Array.new(@capacity)
  end




  def hash(key)
    hash_code = 0
    prime_number = 31
        
    key.each_char { |char| hash_code = prime_number * hash_code + char.ord }
  
    index = hash_code.abs % @capacity
    raise IndexError if index.negative? || index >= @buckets.length
    index
  end

  def length
    count = 0
    @buckets.each do |bucket|
      next if bucket.nil?
      current = bucket
      loop do 
        count += 1
        break if current.next_node.nil?
        current = current.next_node
      end
    end
    count
  end

  def redistribute
    return nil if self.length <= @capacity * @load_factor
    @capacity *= 2
    old_buckets = @buckets
    @buckets = Array.new(@capacity)
    old_buckets.each do |bucket|
      next if bucket.nil?
      current = bucket
      loop do 
        self.set(current.key, current.value)
        break if current.next_node.nil?
        current = current.next_node
      end
    end
  end
  
  def set(key, value)
  index = hash(key)
  current = @buckets[index]
    if current.nil?
      @buckets[index] = Node.new(key, value)
      self.redistribute
      return
    end 


    if current != nil
      loop do 
        if current.key == key 
          current.value = value
          return
        end

        break if current.next_node.nil?
        current = current.next_node
      end
      
      current.next_node = Node.new(key, value)
      self.redistribute

    end
  
  end

  def get(key)
    index = hash(key)
    current = @buckets[index]
    return nil if current.nil?
    loop do 
      return current.value if current.key == key 
      break if current.next_node.nil?
      current = current.next_node
    end
    nil
  end

  def has?(key)
    index = hash(key)
    current = @buckets[index]
    return false if current.nil?
    loop do 
      return true if current.key == key 
      break if current.next_node.nil?
      current = current.next_node
    end
    false
  end

  def remove(key)
    index = hash(key)
    current = @buckets[index]
    previous = nil
    
    return nil if current.nil?



    
    loop do 
      if current.key == key 
        @buckets[index] = current.next_node if previous.nil?

        previous.next_node = current.next_node if previous != nil
        return
      end

      return nil if current.next_node.nil?
      previous = current
      current = current.next_node
    end
  end

  def clear
    @capacity = 16
    @buckets = Array.new(@capacity)
  end

  def keys
    output = []
    @buckets.each do |bucket|
      next if bucket.nil?
      current = bucket
      loop do 
        output.push current.key
        break if current.next_node.nil?
        current = current.next_node
      end
    end
    output
  end

  def values
    output = []
    @buckets.each do |bucket|
      next if bucket.nil?
      current = bucket
      loop do 
        output.push current.value
        break if current.next_node.nil?
        current = current.next_node
      end
    end
    output
  end
end