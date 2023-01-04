#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/eigen.h>
#include <boost/smart_ptr/shared_ptr.hpp>
#include <boost/math/distributions/students_t.hpp>
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

namespace boost{ namespace math{

template <class RealType = double,
          class Policy   = policies::policy<> >
class students_t_distribution;

typedef students_t_distribution<> students_t;

template <class RealType, class Policy>
class students_t_distribution
{
   typedef RealType value_type;
   typedef Policy   policy_type;

   // Construct:
   students_t_distribution(const RealType& v);

   // Accessor:
   RealType degrees_of_freedom()const;

   // degrees of freedom estimation:
   static RealType find_degrees_of_freedom(
      RealType difference_from_mean,
      RealType alpha,
      RealType beta,
      RealType sd,
      RealType hint = 100);
};

}} // namespaces


boost::shared_ptr<int> p1{new int{1}};
//xt::xarray<double> a = xt::random::randn<double>({10}, -0.5, 0.5);



PYBIND11_PLUGIN(inv) {
    pybind11::module m("code", "auto-compiled c++ extension");
    m.def("inv", &inv);
    m.def("lstsq", &lstsq);
    m.def("t_distribution", &students_t_distribution);
    return m.ptr();
}