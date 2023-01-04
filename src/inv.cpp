#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/eigen.h>
#include <boost/smart_ptr/shared_ptr.hpp>
#include <boost/random/normal_distribution.hpp>
//#include <xtensor>
#include <Eigen/LU>
#include <Eigen/Dense>

namespace py = pybind11;

using namespace pybind11::literals;
using namespace std;

#define EIGEN_USE_MKL_ALL

Eigen::MatrixXd inv(Eigen::MatrixXd& xs) {
    return xs.inverse();
}

Eigen::VectorXd lstsq(Eigen::MatrixXd& A, Eigen::VectorXd& b) {
    return (A.transpose() * A).ldlt().solve(A.transpose() * b);
}

template<class T>
double gen_normal(T &generator)
{
  return generator();
}

// template<class T>
// void gen_normal(T &generator,
//               std::vector<double> &res)
// {
//   for(size_t i=0; i<res.size(); ++i)
//     res[i]=generator();
// }

double normal(void)
{
    boost::variate_generator<boost::mt19937, boost::normal_distribution<> >
    generator(boost::mt19937(time(0)),
              boost::normal_distribution<>());
    double r = gen_normal(generator());
  return r;
}

boost::shared_ptr<int> p1{new int{1}};
//xt::xarray<double> a = xt::random::randn<double>({10}, -0.5, 0.5);



PYBIND11_PLUGIN(inv) {
    pybind11::module m("code", "auto-compiled c++ extension");
    m.def("inv", &inv);
    m.def("lstsq", &lstsq);
    m.def("normal", &normal);
    return m.ptr();
}