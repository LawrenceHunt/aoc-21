class LineCalculator

    attr_reader :lines

    def initialize()
        @lines = []
    end

    def add_straight_line(input)
        if LineCalculator.check_straight_line(input)
            @lines.push(input)
        end
    end

    def draw_grid()
        grid = []

        def draw_line(line)
            x1, y1 = line[0]
            x2, y2 = line[1]

            
        end

        @lines.each { |line| draw_line(line) }
    end



    def self.check_straight_line(input)
        x1, y1 = input[0]
        x2, y2 = input[1]
        x1 == x2 or y1 == y2
    end

end